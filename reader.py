import mpyq
from s2protocol import versions
import json
import sys

class Sc2Replay:
    def __init__(self, replay_path):
        self.replay_path = None
        self.archive = None
        self.protocol = None
        self.set_replay(replay_path)
        self.parse_protocol()
        with open('ProductionDuration.json', 'r') as durations:
            self.production_duration = json.load(durations)

    def set_replay(self, replay_path, parse_protocol=True):
        self.replay_path = replay_path
        self.archive = mpyq.MPQArchive(replay_path)
        if parse_protocol:
            self.parse_protocol()

    def parse_protocol(self):
        archive_header = self.archive.header['user_data_header']['content']
        decoded_header = versions.latest().decode_replay_header(archive_header)
        base_build = decoded_header['m_version']['m_baseBuild']
        self.protocol = versions.build(base_build)
        return self.protocol

    def parse_player_productions(self, use_json=False):
        tracker_events = self.archive.read_file('replay.tracker.events')
        decoded_tracker_events = self.protocol.decode_replay_tracker_events(tracker_events)
        player_productions = {player_id: [] for player_id in range(1, 17)}
        for event in decoded_tracker_events:
            if event['_gameloop'] > 0:
                event_name = event['_event']
                player_id = None
                if 'm_controlPlayerId' in event:
                    player_id = event['m_controlPlayerId']
                elif 'm_playerId' in event:
                    player_id = event['m_playerId']

                # structures start building or units start warping
                if event_name == 'NNet.Replay.Tracker.SUnitInitEvent':
                    player_productions[player_id].append({'loop': event['_gameloop'], 'name': event['m_unitTypeName']})
                # units training
                elif event_name == 'NNet.Replay.Tracker.SUnitBornEvent' and \
                        event['m_unitTypeName'] in self.production_duration['unit']:
                    start_time = event['_gameloop'] - self.production_duration['unit'][event['m_unitTypeName']] * 16
                    player_productions[player_id].append({'loop': start_time, 'name': event['m_unitTypeName']})
                # researches
                elif event_name == 'NNet.Replay.Tracker.SUpgradeEvent' and \
                        event['m_upgradeTypeName'] in self.production_duration['tech']:
                    start_time = event['_gameloop'] - self.production_duration['tech'][event['m_upgradeTypeName']] * 16
                    player_productions[player_id].append({'loop': start_time, 'name': event['m_upgradeTypeName']})

        return player_productions if not use_json else json.dumps(player_productions)


if __name__ == '__main__':
    try:
        rep = Sc2Replay(sys.argv[1])
        productions = rep.parse_player_productions(True)
        filename = sys.argv[1].replace(".SC2Replay","") + ".json"
        file = open(filename,"w")
        file.write(productions)
        file.close()
    except:
        print ""
    else:
        print ""
import json

if __name__ == '__main__':
    productionDuration = {
        'unit': {
            'SCV': 17,
            'Marine': 25,
            'Marauder': 30,
            'Reaper': 45,
            'Ghost': 40,
            'Hellion': 30,
            'Siege Tank': 45,
            'Thor': 60,
            'Viking': 42,
            'Medivac': 42,
            'Raven': 60,
            'Banshee': 60,
            'Battlecruiser': 90,
            'Hellbat': 30,
            'Widow Mine': 40,
            'Liberator': 60,
            'Cyclone': 32,

            'Drone': 17,
            'Overlord': 25,
            'Zergling': 24,
            'Queen': 50,
            'Hydralisk': 33,
            'Baneling': 20,
            'Overseer': 17,
            'Roach': 27,
            'Infestor': 50,
            'Mutalisk': 33,
            'Corruptor': 40,
            'Nydus Worm': 20,
            'Ultralisk': 55,
            'Brood Lord': 34,
            'Swarm Host': 40,
            'Viper': 40,
            'Ravager': 9,
            'Lurker': 15,

            'Probe': 17,
            'Zealot': 38,
            'Stalker': 42,
            'Sentry': 37,
            'Observer': 30,
            'Immortal': 55,
            'Warp Prism': 50,
            'Colossus': 75,
            'Phoenix': 35,
            'Void Ray': 60,
            'High Templar': 55,
            'Dark Templar': 55,
            'Archon': 12,
            'Carrier': 120,
            'Mothership': 100,
            'Mothership Core': 30,
            'Oracle': 50,
            'Tempest': 60,
            'Adept': 38,
            'Disruptor': 50,
        },

        'tech': {
            'TerranInfantryWeaponsLevel1': 114,
            'TerranInfantryWeaponsLevel2': 136,
            'TerranInfantryWeaponsLevel3': 157,
            'TerranVehicleWeaponsLevel1': 114,
            'TerranVehicleWeaponsLevel2': 136,
            'TerranVehicleWeaponsLevel3': 157,
            'TerranShipWeaponsLevel1': 114,
            'TerranShipWeaponsLevel2': 136,
            'TerranShipWeaponsLevel3': 157,
            'TerranInfantryArmorsLevel1': 114,
            'TerranInfantryArmorsLevel2': 136,
            'TerranInfantryArmorsLevel3': 157,
            'TerranVehicleAndShipArmorsLevel1': 0,
            'TerranVehicleAndShipArmorsLevel2': 0,
            'TerranVehicleAndShipArmorsLevel3': 0,

            'ProtossGroundWeaponsLevel1': 160,
            'ProtossGroundWeaponsLevel2': 190,
            'ProtossGroundWeaponsLevel3': 220,
            'ProtossAirWeaponsLevel1': 160,
            'ProtossAirWeaponsLevel2': 190,
            'ProtossAirWeaponsLevel3': 220,
            'ProtossGroundArmorsLevel1': 160,
            'ProtossGroundArmorsLevel2': 190,
            'ProtossGroundArmorsLevel3': 220,
            'ProtossAirArmorsLevel1': 160,
            'ProtossAirArmorsLevel2': 190,
            'ProtossAirArmorsLevel3': 220,
            'ProtossShieldsLevel1': 160,
            'ProtossShieldsLevel2': 190,
            'ProtossShieldsLevel3': 220,

            'ZergMeleeWeaponsLevel1': 160,
            'ZergMeleeWeaponsLevel2': 190,
            'ZergMeleeWeaponsLevel3': 220,
            'ZergMissileWeaponsLevel1': 160,
            'ZergMissileWeaponsLevel2': 190,
            'ZergMissileWeaponsLevel3': 220,
            'ZergFlyerWeaponsLevel1': 160,
            'ZergFlyerWeaponsLevel2': 190,
            'ZergFlyerWeaponsLevel3': 220,
            'ZergGroundArmorsLevel1': 160,
            'ZergGroundArmorsLevel2': 190,
            'ZergGroundArmorsLevel3': 220,
            'ZergFlyerArmorsLevel1': 160,
            'ZergFlyerArmorsLevel2': 190,
            'ZergFlyerArmorsLevel3': 220,

            'Stimpack': 0,
            'HighCapacityBarrels': 0,
            'ShieldWall': 0,
            'PunisherGrenades': 0,
            'MedivacIncreaseSpeedBoost': 0,
            'CycloneRapidFireLaunchers': 0,
            'BansheeSpeed': 0,
            'BansheeCloak': 0,
            'DrillClaws': 0,
            'BattlecruiserEnableSpecializations': 0,
            'RavenCorvidReactor': 0,
            'LiberatorAGRangeUpgrade': 0,
            'SmartServos': 0,
            'PersonalCloaking': 0,
            'HiSecAutoTracking': 0,
            'NeosteelFrame': 0,
            'TerranBuildingArmor': 0,

            'WarpGateResearch': 160,
            'AdeptPiercingAttack': 0,
            'PsiStormTech': 0,
            'Charge': 0,
            'DarkTemplarBlinkUpgrade': 0,
            'ExtendedThermalLance': 0,
            'GraviticDrive': 0,
            'BlinkTech': 0,
            'CarrierLaunchSpeedUpgrade': 0,
            'PhoenixRangeUpgrade': 0,
            'ObserverGraviticBooster': 0,

            'zerglingmovementspeed': 0,
            'GlialReconstitution': 0,
            'InfestorEnergyUpgrade': 0,
            'TunnelingClaws': 0,
            'NeuralParasite': 0,
            'EvolveGroovedSpines': 0,
            'zerglingattackspeed': 0,
            'overlordspeed': 0,
            'EvolveMuscularAugments': 0,
            'Burrow': 0,
            'DiggingClaws': 0,
            'ChitinousPlating': 0,
        }
    }

    with open('ProductionDuration.json', 'w') as file:
        file.write(json.dumps(productionDuration))
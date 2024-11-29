import os
import re

def replace_words_in_folder(root_folder, replacements):
    """
    Replace exact words in all files in a folder and its subdirectories based on a dictionary.

    - Creates a backup of each original file with `.bak` appended to the file name.
    - Saves the modified file with the original name.

    :param root_folder: Root folder to start processing.
    :param replacements: Dictionary where keys are words to search for (case-sensitive),
                         and values are words/phrases to replace them with.
    """
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            # Skip Python scripts, DLL, and EXE files
            if filename.endswith(('.py', '.dll', '.exe', '.bak')):
                continue

            file_path = os.path.join(dirpath, filename)
            
            try:
                # Read the original file
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # Backup the original file
                backup_path = f"{file_path}.bak"
                with open(backup_path, 'w', encoding='utf-8') as backup_file:
                    backup_file.write(content)
                
                # Perform replacements
                modified_content = content
                for old_word, new_word in replacements.items():
                    # Create regex patterns for exact matches with word boundaries (case-sensitive)
                    pattern = re.compile(rf'\b{re.escape(old_word)}\b')
                    modified_content = pattern.sub(new_word, modified_content)
                
                # Save the modified file with the original name
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(modified_content)
                
                print(f"Processed: {file_path}")
            
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

# Example usage
root_folder = '.'  # Replace with your root folder path
replacements = {
    "sevenkingdoms": "dynamo",
    "SEVENKINGDOMS": "DYNAMO",
    "kingslanding": "dynamo-dc01",
    "robert.baratheon": "roberto.perez",
    "Robert": "Roberto",
    "Robert Baratheon": "Roberto Perez",
    "cersei.lannister": "maria.lopez",
    "DragonRider": "DynamoFriend",
    "Small Council": "WarehouseOps",
    "Baratheon": "HRTeam",
    "renly.baratheon": "manuel.perez",
    "renly": "manuel",
    "Renly": "Manuel",
    "lorastyrell": "arrozConPollo",
    "Renly Baratheon": "Manuel Perez",
    "winterfell": "finance-dc02",
    "eddard.stark": "jose.garcia",
    "catelyn.stark": "laura.garcia",
    "robb.stark": "jesus.garcia",
    "Stark": "Garcia",
    "castelblack": "warehouse-srv02",
    "sexywolfy": "noGuard4r",
    "jeor.mormont": "ivan.martinez",
    "Mormont": "TransportManagers",
    "arya.stark": "maria.garcia",
    "arya": "maria",
    "Arya": "Maria",
    "Arya Stark": "Maria Garcia",
    "jon.snow": "juan.iniesta",
    "Needle": "quieroNoPuedo",
    "Winterfell": "Madrid" ,
    "Eddard Stark": "Jose Garcia",
    "Eddard": "Jose",
    "FightP3aceAndHonor!": "cieloAzulSalvaje",
    "King's Landing": "Barcelona",
    "Catelin Stark": "Laura Garcia",
    "Catelyn": "Laura",
    "robbsansabradonaryarickon": "jesuslauramariapedro",
    "Robb Stark": "Jesus Garcia",
    "Robb": "Jesus",
    "sansa.stark": "susana.garcia",
    "Sansa": "Susana",
    "Sansa Stark": "Susana Garcia",
    "eyrie": "villatoro",
    "brandon.stark": "vicente.garcia",
    "Brandon": "Vicente",
    "Brandon Stark": "Vicente Garcia",
    "rickon.stark": "raul.garcia",
    "Rickon": "Raul",
    "Rickon Stark": "Raul Garcia",
    "Winter2022": "Verano2025",
    "hodor": "pepe",
    "Brainless Giant": "El becario",
    "Jon Snow": "Juan Iniesta",
    "Jon": "Juan",
    "Castel Black": "Burgos",
    "Night Watch": "ITSupport",
    "thewall": "firewall",
    "Samwell Tarly": "Samuel Tejero",
    "Samwell": "Samuel",
    "Tarly": "Tejero",
    "samwell.tarly": "samuel.tejero",
    "Heartsbane": "Espadas",
    "Samwell Tarly (Password : Heartsbane)": "Samuel Tejero (Contraseña: Espadas)",
    "Jeor Mormont": "Ivan Martinez",
    "Jeor": "Ivan",
    "Mormont": "Martinez",
    "Lannister": "Lopez",
    "Lanister": "Lopez",
    "tywin.lannister": "kiko.lopez",
    "Tywin": "Kiko",
    "Tywin Lannister": "Kiko Lopez",
    "Baratheon": "Perez",
    "Westerlands": "Andalucia",
    "Stormlands": "Catalunna",
    "Crownlands": "CMadrid",
    "IronIslands": "Baleares",
    "Riverlands": "Galicia",
    "Reach": "CValencia",
    "Vale": "Murcia",
    "Dorne": "Canarias",
    "DragonStone": "Gamonal",
    "KingsGuard": "WarehouseGuards",
    "AcrossTheNarrowSea": "NorthPeople",
    "forcechangepassword_tywin_jaime": "cambiodecontrasena_kiko_jaime",
    "jaime.lannister": "jaime.lopez",
    "Jaime": "Jaime",
    "Jaime Lannister": "Jaime Lopez",
    "Lannister": "Lopez",
    "GenericWrite_on_user_jaimie_javier": "EscrituraGenerica_en_usuario_jaime_javier",
    "joffrey.baratheon": "javier.lopez",
    "Joffrey": "Javier",
    "Joffrey Baratheon": "Javier Lopez",
    "Writedacl_joffrey_tyron": "EscribirListaControlAcceso_javier_daniel",
    "tyron.lannister": "daniel.lopez",
    "Tyron": "Daniel",
    "Tyron Lannister": "Daniel Lopez",
    "self-self-membership-on-group_tyron_small_council": "autoautoasociacion-en-grupo_daniel_warehouseops",
    "addmember_smallcouncil_DragonStone": "agregarmiembro_warehouseops_Gamonal",
    "write_owner_dragonstone_kingsguard": "escribir_propietario_gamonal_warehouseguards",
    "GenericAll_kingsguard_stanis": "GenericAll_warehouseguards_sandra",
    "stannis.baratheon": "sandra.perez",
    "Stannis": "Sandra",
    "Stannis Baratheon": "Sandra Perez",
    "Drag0nst0ne": "Gam0nal",
    "GenericAll_stanis_dc": "GenericAll_sandra_dc",
    "GenericAll_group_acrrosdom_dc": "GenericAll_grupo_northpeople_dc",
    "GenericAll_varys_domadmin": "GenericAll_vega_administradordominio",
    "lord.varys": "lord.vega",
    "Varys": "Vega",
    "Lord Varys": "Lord Vega",
    "GenericAll_varys_domadmin_holder": "GenericAll_vega_administradordominio_portador",
    "WriteDACL_renly_Crownlands": "WriteDACL_manuel_CMadrid",
    "Casterly Rock": "Sevilla",
    "cersei": "carla",
    "cersei.lannister": "carla.lopez",
    "Cersei": "Carla",
    "Cersei Lannister": "Carla Lopez",
    "petyer.baelish": "particio.burguense",
    "Petyer": "Particio",
    "Baelish": "Burguense",
    "Petyer Baelish": "Particio Burguense",
    "maester.pycelle": "maestro.paellero",
    "Pycelle": "Paellero",
    "Maester Pycelle": "Maestro Paellero",
    "Maester": "Maestro",
    }

replace_words_in_folder(root_folder, replacements)

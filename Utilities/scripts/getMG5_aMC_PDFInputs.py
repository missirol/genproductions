from PDFSetsChooserTools import PDFSetHelper_MG5_aMC
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--format', choices=['systematics', 'central', 'members', 'sets'], 
        required=True, help='Output PDF set list or list of members to store')
parser.add_argument('-c', '--pdf_choice', choices=['custom', '2016', '2017'],
        required=True, help="Use 2017 or 2016 defaults or custom choice")
parser.add_argument('-n', '--nFlavorScheme', action='store', type=int, choices=[3, 4, 5], default=4,
        help='Flavor Scheme: number of quark flavors in the initial state [must be 3, 4 (default), or 5]')
parser.add_argument('--isNLO', action='store_true',
        help='NLO vs. LO MG5_aMC@NLO')

args = parser.parse_args()

helper = PDFSetHelper_MG5_aMC()
if args.pdf_choice == '2017':
    helper.readDefaultPDFsFile(args.FlavorScheme)
else:
    #TODO Implement option for custom PDF list
    print "Custom sets not yet supported!"
    exit(1)

if args.format == "central":
    print helper.getListOfLHAPDFIds(False)

elif args.format == "sets":
    print helper.getListOfLHAPDFIds(args.isNLO)

elif args.format == "members":
    # Only used for NLO 
    print helper.getListOfMembersToStore()

# Format pdf list for systematics program
# See https://cp3.irmp.ucl.ac.be/projects/madgraph/wiki/Systematics
elif args.format == "systematics":
    print helper.getListOfLHAPDFIdsForSystematics()

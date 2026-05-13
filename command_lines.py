def hello(name,lang):
    greetings={
        "English":"Hello",
        "Spanish":"Hola",
        "German":"Hallo",
    }
    message =f"{greetings[lang]} {name}"
    print(message)

if __name__ == '__main__':

    import argparse #commandline option and argumen tparsing library

    parser = argparse.ArgumentParser(
        description='provides a personal greeting'
    )
    parser.add_argument(
        '-n','--name',metavar='name',
        required=True,help='The name of the person to greet'
    )
    parser.add_argument(
        '-l','--lang',metavar='language',
        required=True,choices=['English','Spanish','German'],
        help='language of the greeting'
    )
    args = parser.parse_args()

    hello(args.name,args.lang)
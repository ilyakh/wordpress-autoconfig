from subprocess import call

class shell:
    def __lt__( self, argument_list ):
        call( argument_list )

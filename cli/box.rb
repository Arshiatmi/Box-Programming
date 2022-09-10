help_string = <<END_HELP
You Need To Insert Command.
Usage :
	box.rb command [arguments]

Commands :
	install    ->   To Install Extention. It Needs One Argument Containing Extention Name.
	uninstall  ->   To Remove Extention. It Needs One Argument Containing Extention Name.
	verify     ->   It Will Verify All Of Your Extentions And Warns You On Unverified Extentions.
	list       ->   Gets Extention List For You.
	search     ->   Search For Your Extention. Needs One Argument As Extention Name.
	help       ->   Show This Help Message.
END_HELP



command = ARGV[0]
if not command
	puts help_string
	exit(1)
end


def help_command
	puts help_string
end

def install(name)
	if name
		puts "Installing " + name
	else
		puts "You Need To Insert Argument For Your Command Too ( Extention Name )."
	end
end

def uninstall(name)
	if name
		puts "Uninstalling " + name
	else
		puts "You Need To Insert Argument For Your Command Too ( Extention Name )."
	end
end

def verify(name)
	if name
		puts "Verifing " + name
	else
		puts "You Need To Insert Argument For Your Command Too ( Extention Name )."
	end
end

def list
	puts "Extention List"
end

def search(name)
	if name
		puts "Searching " + name
	else
		puts "You Need To Insert Argument For Your Command Too ( Extention Name )."
	end
end

case command
when "install"
	install(ARGV[1])
when "uninstall"
	uninstall(ARGV[1])
when "verify"
	verify(ARGV[1])
when "list"
	list
when "help"
	help_command
when "search"
	search(ARGV[1])
else
	puts "There Is No Command " + command
	exit(2)
end

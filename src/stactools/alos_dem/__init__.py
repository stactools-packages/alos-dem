from stactools.core import io

io.use_fsspec()


def register_plugin(registry):
    from stactools.alos_dem import commands
    registry.register_subcommand(commands.create_alos_dem_command)


__version__ = "0.1.2"

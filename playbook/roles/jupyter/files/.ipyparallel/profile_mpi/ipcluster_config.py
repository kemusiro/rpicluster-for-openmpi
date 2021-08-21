# c.Application.log_level = 'DEBUG'
# c.BaseIPythonApplication.log_level = "DEBUG"
# c.BaseParallelApplication.log_level = "DEBUG"
# c.BaseParallelApplication.log_to_file = True
c.IPClusterEngines.engine_launcher_class = 'MPIEngineSetLauncher'
# c.IPClusterEngines.log_level = 'DEBUG'
# c.IPClusterEngines.log_to_file = True
c.IPClusterStart.controller_launcher_class = 'MPIControllerLauncher'
c.IPClusterStart.engine_launcher_class = 'MPIEngineSetLauncher'
# c.IPClusterStart.log_level = 'DEBUG'
# c.IPClusterStart.log_to_file = True
# c.LocalEngineSetLauncher.engine_args = ['--log-level="DEBUG"']
c.MPILauncher.mpi_args = ['--hostfile', '/share/.ipyparallel/hostfile']
# Default: ['--log-level="DEBUG"', "--ip='*'"]
c.MPIControllerLauncher.mpi_args = ['--hostfile', '/share/.ipyparallel/hostfile']
# c.MPIEngineSetLauncher.engine_args = ['--log-level="DEBUG"']
c.MPIEngineSetLauncher.mpi_args = ['--hostfile', '/share/.ipyparallel/hostfile']


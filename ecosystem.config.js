module.exports = {
    apps: [
      {
        name: "rande",
        script: "gunicorn",
	      interpreter: "python",
	      interpreter_args: "-u",
        max_memory_restart: "256M",
        kill_timeout: 5000,
        restart_delay: 5000
      }
    ]
  }

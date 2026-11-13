module.exports = {
    apps: [
      {
        name: "rande",
        script: ".venv/bin/gunicorn",
        interpreter: ".venv/bin/python",
	interpreter_args: "-u",
        max_memory_restart: "256M",
        kill_timeout: 5000,
        restart_delay: 5000
      }
    ]
  }

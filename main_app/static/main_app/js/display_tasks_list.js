function show_tasks_list() {
    document.getElementById("main").innerHTML = ""
    fetch("/tasks/")
        .then(response => response.json())
        .then(tasks => {
            for (let i = 0; i < tasks.length; i++) {
                var div = document.createElement('DIV');
                var task_link = `<a style="text-decoration: none;"  href="/tasks/${tasks[i]["task_id"]}/">
                              <h2 class="h2-outline" style="color: gold; margin: 20px;">${tasks[i]["task_title"]}`
                if (tasks[i]["level_of_task_difficulty"] === "True") {
                    task_link = task_link + ` (completed) | `
                } else {
                    task_link = task_link + ` | `
                }

                if (tasks[i]["level_of_task_difficulty"] === "Easy") {
                    div.innerHTML = task_link + `<p style="color: green; display: inline;">
                                    ${tasks[i]["level_of_task_difficulty"]}</p></h2>`;
                } else if (tasks[i]["level_of_task_difficulty"] === "Medium") {
                    div.innerHTML = task_link + `<p style="color: orange; display: inline;">
                                    ${tasks[i]["level_of_task_difficulty"]}</p></h2>`;
                } else {
                    div.innerHTML = task_link + `<p style="color: black; display: inline;">
                                    ${tasks[i]["level_of_task_difficulty"]}</p></h2>`;
                }
                document.getElementById("main").appendChild(div);
            }
        })
}
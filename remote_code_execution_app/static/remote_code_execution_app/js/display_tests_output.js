$(document).ready(function () {
    $('textarea').keydown(function (e) {
        if (e.keyCode === 9) {
            const start = this.selectionStart;
            const end = this.selectionEnd;
            const $this = $(this);
            const value = $this.val();
            $this.val(value.substring(0, start) + '\t' + value.substring(end));
            this.selectionStart = this.selectionEnd = start + 1;
            e.preventDefault();
        }
    });

    $("#check-button").click(function (event) {
        const data = encodeURIComponent(document.getElementById('code_editor').value);
        document.getElementById("output").innerHTML = "<p class='test-case-output-style-text'>Loading...</p>";
        $.ajax({
            url: `/tasks/compile/?code=${data}&task=${task_id}&token=${task_token}`,
            type: "get",
            processData: false,
            contentType: false,
            success: function (data) {
                const output = document.getElementById("output");
                const amount_of_test_cases = data["amount_of_test_cases"];
                const amount_of_passed_test_cases = data["amount_of_passed_test_cases"];
                if (amount_of_test_cases === amount_of_passed_test_cases) {
                    document.getElementById("output").innerHTML = `<p class='test-case-output-style-text'>` +
                        `Test results: <span style="color: green;">${amount_of_passed_test_cases}/${amount_of_test_cases}<span></p>`;
                } else {
                    document.getElementById("output").innerHTML = `<p class='test-case-output-style-text'>` +
                        `Test results: <span style="color: red;">${amount_of_passed_test_cases}/${amount_of_test_cases}<span></p>`;
                }
                for (let test_number = 1; test_number <= amount_of_test_cases; test_number++) {
                    const div = document.createElement("DIV");
                    const current_test_case = data["test_case_" + test_number];
                    if (current_test_case) {
                        div.innerHTML = `<h5 style="color: green;">Test Case ${test_number}</h5><p style="color: green;">PASSED</p><br>`;
                    } else {
                        div.innerHTML = `<h5 style="color: red;">Test Case ${test_number}</h5><p style="color: red;">FAILED</p><br>`;
                    }
                    output.appendChild(div);
                }
            },
        })
    });

    $("#submit-button").click(function (event) {
        const data = encodeURIComponent(document.getElementById('code_editor').value);
        document.getElementById("output").innerHTML = "<p class='test-case-output-style-text'>Loading...</p>";
        $.ajax({
            url: `/tasks/compile/?code=${data}&task=${task_id}&token=${task_token}`,
            type: "get",
            processData: false,
            contentType: false,
            success: function (data) {
                const div = document.createElement("DIV");
                const output = document.getElementById("output");
                const all_test_passed = data["all_tests_passed"];
                const user_amounts_of_try = data["user_amounts_of_try"];
                if (all_test_passed) {
                    output.innerHTML =
                        `<h4 style='color: green;'>Congratulations your code has passed all the tests! You completed 
                        the task on the <span style="color: gold;">${user_amounts_of_try}</span> try!</h4>`;
                } else {
                    output.innerHTML = "<h4 style='color: red;'>Unfortunately, your code didn't pass all tests!</h4>";
                }
                output.appendChild(div);
            },
        })
    });
});
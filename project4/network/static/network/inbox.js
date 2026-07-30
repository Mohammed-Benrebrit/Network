
document.addEventListener("DOMContentLoaded", function () {

    // edit
    const alledits = document.querySelectorAll("#bt")
    alledits.forEach(function (i) {

        i.addEventListener('click', () => {
            var postid = i.value;
            var cont = document.getElementById(`tx-${postid}`).textContent
            document.getElementById(`tx-${postid}`).style.display = 'none'
            document.getElementById(`edt-${postid}`).style.display = 'block'
            document.getElementById(`edt-${postid}`).value = cont
            document.getElementById(`sav-${postid}`).style.display = 'block'


            document.getElementById(`sav-${postid}`).addEventListener('click', () => {
                var newtx = document.getElementById(`edt-${postid}`).value;
                fetch('/profile/<str:uname>', {
                    method: 'PUT',
                    body: JSON.stringify({
                        pid: `${postid}`,
                        ntx: `${newtx}`
                    })
                })
                    .then(response => response.json())
                    .then(result => {
                        // Print result
                        console.log(result);
                    });

                document.getElementById(`tx-${postid}`).style.display = 'block'
                document.getElementById(`tx-${postid}`).textContent = newtx
                document.getElementById(`edt-${postid}`).style.display = 'none'
                document.getElementById(`sav-${postid}`).style.display = 'none'
            })

        })

    })

    const ff = document.getElementById('f')
    if (ff !== null) {
        ff.addEventListener('submit', function (e) {
            e.preventDefault();
            const usn = document.getElementById('usn').value
            const check = document.getElementById('usn1').value

            if (check === 't') {
                fetch('/profile/<str:uname>', {
                    method: 'POST',
                    body: JSON.stringify({
                        usn: `${usn}`,
                        check: `${check}`
                    })
                })
                    .then(response => response.json())
                    .then(result => {
                        // Print result
                        console.log(result);
                    });
                // increas number of followers
                var n = document.getElementById('folw');
                var nn = parseInt(n.textContent) + 1
                n.innerHTML = nn
                // 
                document.getElementById('usn1').value = 'f';
                document.getElementById('sv').value = 'unfollow';
            }

            else {
                fetch('/profile/<str:uname>', {
                    method: 'POST',
                    body: JSON.stringify({
                        usn: `${usn}`,
                        check: `${check}`
                    })
                })
                    .then(response => response.json())
                    .then(result => {
                        // Print result
                        console.log(result);
                    });

                //
                var n = document.getElementById('folw');
                var nn = parseInt(n.textContent) - 1
                n.innerHTML = nn
                // 
                document.getElementById('sv').value = 'follow'
                document.getElementById('usn1').value = 't'
            }
        });

    }


});

document.addEventListener("DOMContentLoaded", function () {

    let lid = document.querySelectorAll('#lid')
    lid.forEach(function (i) {
        let lid1 = i.value
        var c = document.getElementById(`l-${lid1}`)
        if (c !== null) {
            document.getElementById(`dl-${lid1}`).style.display = "block"
            document.getElementById(`ch-${lid1}`).value = 't'
        }
        else {
            document.getElementById(`dd-${lid1}`).style.display = "block"
            document.getElementById(`ch-${lid1}`).value = 'f'
        }
    })

    const l = document.querySelectorAll("#like")
    l.forEach(function (i) {
        i.addEventListener('click', () => {

            var id = i.value
            fetch('/followings', {
                method: 'PUT',
                body: JSON.stringify({
                    pid: `${id}`
                })
            })
                .then(response => response.json())
                .then(result => {
                    // Print result
                    console.log(result);
                });
            let check = document.getElementById(`ch-${id}`).value
            if (check === 'f') {
                i.classList.add('liked');
                i.classList.remove('button-like');
                document.getElementById(`ch-${id}`).value = 't'
                var nlid = document.querySelectorAll(`#n-${id}`)
                nlid.forEach(function (s) {
                    var nl = parseInt(s.textContent) + 1
                    s.textContent = nl
                })

                console.log('add-liked')
            }
            else {
                i.classList.add('button-like');
                i.classList.remove('liked');
                document.getElementById(`ch-${id}`).value = 'f'
                var nlid = document.querySelectorAll(`#n-${id}`)
                nlid.forEach(function (s) {
                    var nl = parseInt(s.textContent) - 1
                    s.textContent = nl
                })
                console.log('remov-like')
            }

        })
    })


})
 document.getElementById('formularioContacto').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Reset errores
            document.querySelectorAll('.error').forEach(el => el.style.display = 'none');
            document.querySelectorAll('.form-control').forEach(el => el.classList.remove('error-input'));
            
            // Validación
            let isValid = true;
            const nombre = document.getElementById('nombre');
            const email = document.getElementById('email');
            const mensaje = document.getElementById('mensaje');
            const asunto = document.getElementById('asunto');

            if (!asunto.value.trim()) {
                document.getElementById('errorAsunto').style.display = 'block';
                asunto.classList.add('error-input');
                isValid = false;
            }
            
            if (!nombre.value.trim()) {
                document.getElementById('errorNombre').style.display = 'block';
                nombre.classList.add('error-input');
                isValid = false;
            }
            
            if (!email.value.trim() || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) {
                document.getElementById('errorEmail').style.display = 'block';
                email.classList.add('error-input');
                isValid = false;
            }
            
            if (!mensaje.value.trim()) {
                document.getElementById('errorMensaje').style.display = 'block';
                mensaje.classList.add('error-input');
                isValid = false;
            }
            
            if (isValid) {
                
                fetch('/enviar-formulario', {
                    method: 'POST',
                    body: new FormData(this)
                })
                .then(response => response.json())
                .then(data => {
                    if(data.message){
                        alert(data.message);
                    this.reset();
                    }else if (data.error){
                        alert('Error:'+data.error);
                    }                       
                })
                .catch(error => {
                    console.error('Error al enviar el formulario:', error);
                    alert('Error al enviar el formulario. Por favor, inténtalo de nuevo más tarde.');  
                });
            }
        });
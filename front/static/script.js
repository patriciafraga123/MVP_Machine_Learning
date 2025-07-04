/*
Projeto: Machine Learning Avaliação de Personalidade
Autor: Patricia Fraga Ferreira
Data: Julho/2025

Script JavaScript para enviar as respostas do questionário ao backend Flask,
receber a predição da personalidade e exibir o resultado ao usuário em um modal.
*/

function fecharModal() {
    document.getElementById('modalResultado').style.display = 'none';
}

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('formulario');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const formData = new FormData(form);
        const entrada = [
            parseInt(formData.get('time_alone')),
            parseInt(formData.get('stage_fear')),
            parseInt(formData.get('social_event')),
            parseInt(formData.get('going_outside')),
            parseInt(formData.get('drained_after')),
            parseInt(formData.get('friends_circle')),
            parseInt(formData.get('post_frequency'))
        ];

        try {
            const response = await fetch('/prever', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ entrada })
            });

            const data = await response.json();

            if (response.ok) {
                // Mapeia as respostas em inglês para português
                const traducoes = {
                    'Introvert': 'Introvertido(a)',
                    'Extrovert': 'Extrovertido(a)',
                    // Caso backend já retorne em português, mantém igual
                    'Introvertido(a)': 'Introvertido(a)',
                    'Extrovertido(a)': 'Extrovertido(a)'
                };

                const resultadoTraduzido = traducoes[data.predicao] || data.predicao;

                // Preenche o texto do modal e exibe
                document.getElementById('textoResultado').innerText = resultadoTraduzido;
                document.getElementById('modalResultado').style.display = 'flex';

                // Reseta o formulário
                form.reset();
            } else {
                alert(`Erro: ${data.erro || 'Erro desconhecido'}`);
            }
        } catch (error) {
            alert('Erro ao conectar ao servidor');
        }
    });
});

async function handleSubmit(e)
{
    e.preventDefault();
    console.log(e.target.preg.value)
    console.log(e.target.glucose.value)
    console.log(e.target.bp.value)
    console.log(e.target.skinthick.value)
    console.log(e.target.insulin.value)
    console.log(e.target.bmi.value)
    console.log(e.target.pedifunc.value)
    console.log(e.target.age.value)

    const ob = {Pregnancies: e.target.preg.value,
        Glucose: e.target.glucose.value,
        BP: e.target.bp.value,
        Skinthickness: e.target.skinthick.value,
        Insulin: e.target.insulin.value,
        BMI: e.target.bmi.value,
        pedi: e.target.pedifunc.value,
        Age: e.target.age.value
    }

    const resp = await fetch('https://diabetes-predictor-ecru.vercel.app/back', {
        method: 'POST',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(ob)
    })
    const res = await resp.json()
    console.log(res.message)

    const head = document.querySelector('#print')
    head.innerText ="Patient maybe: " + res.message

    document.querySelector('#form').reset();
}
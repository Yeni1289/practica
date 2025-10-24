from django.shortcuts import render

def examen(request):
    # Valores por defecto
    x = 0
    y = 0
    resultado = None
    z = None
    x_final = None
    x0 = None
    y0 = None

    if request.method == "POST":
        try:
            x_input = int(request.POST.get("x", 0))
            y_input = int(request.POST.get("y", 0))

            # Guardamos valores originales
            x0 = x_input
            y0 = y_input

            # Operaciones
            z = x0 * y0 + 10
            x_final = x0 + 1

            # No alteramos los inputs para que no se incremente en cada submit
            x = x0
            y = y0
            resultado = True
        except ValueError:
            resultado = None

    return render(request, "core/index.html", {
        "x": x,
        "y": y,
        "resultado": resultado,
        "z": z,
        "x_final": x_final,
        "x0": x0,
        "y0": y0
    })

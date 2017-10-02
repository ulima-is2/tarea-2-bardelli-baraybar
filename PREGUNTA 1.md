## 1. Principio de Responsabilidad Única
 Consideramos que se está violando el principio de responsabilidad única
 debido a que las clases _"CineStark"_ y _"CinePlaneta"_
 realizan operaciones que si bien están relacionadas,
 aumentan la cantidad de métodos de las que las clases
 están hechas. <br/><br/>
 Se crearon las clases solo para tener
 un objeto de ellos. Se debería implementar una clase
 de gestión para las películas, funciones y entradas respectivamente.
## 2. Principio Open-Close
 Debido a que existe más de un tipo de cine, la solución a la violación de este principio
 es mediante el uso de abstracciones (una clase padre Cine), en las que nuestros cines comparten propiedades y métodos
 (como películas, funciones, etc.).<br/><br/>
 De esta manera, a la hora de llamar a las operaciones para listar películas o funciones,
 a estos no les importará el tipo de cine que sea, solamente importará cumplir con la interfaz padre. De esta forma,
 en un futuro en el cual más cines se unan, solo tendremos que preocuparnos por que los nuevos cines cumplan con el padre.
## 3. Principio Interface Segregation
 En el caso del código proporcionado, se está violando el principio de segregación de
 interfaces ya que se debe usar clases más pequeñas que se hereden de la clase _"Cine"_
 y que cada una implemente sus propios métodos en lugar de que una clase herede pequeña
 herede métodos que no va a usar necesariamente.

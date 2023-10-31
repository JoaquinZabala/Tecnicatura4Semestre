import  Router  from "express-promise-router";
import {actualizarTarea, crearTarea, eliminarTarea, listarTarea, listarTarea} from "../controllers/tarea.controller.js"
import {isAuth} from "../middlewares/auth.middleware.js"

const router = Router();

router.get('/tareas',isAuth,listarTarea);

router.get('/tareas/:id',isAuth,listarTarea);

router.post('/tareas',isAuth,crearTarea)

router.put('/tareas/:id',isAuth,actualizarTarea);

router.delete('/tarea/:id',isAuth,eliminarTarea );

export default router;

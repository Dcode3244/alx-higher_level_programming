#include <Python.h>

/**
 * print_python_list_info - prints some basic info about python lists
 * @p: the python list
 */
void print_python_list_info(PyObject *p)
{
	int i, size;
	PyObject *type;

	size = (int)PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		type = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(type)->tp_name);
	}
}

from .backend import Backend

class SolverBackend(Backend):
	def __init__(self):
		Backend.__init__(self)

	#
	# These functions provide solving and evaluation support.
	#

	def solver(self, timeout=None):
		'''
		This function should return an instance of whatever object handles
		solving for this backend. For example, in Z3, this would be z3.Solver()
		'''
		raise NotImplementedError("backend doesn't support solving")

	def add_exprs(self, s, c):
		'''
		This function adds constraints to the backend solver.

		@param c: sequence of claripy.E objects
		@param s: backend solver object
		'''
		return self.add(s, self.convert_list(c))

	def add(self, s, c):
		'''
		This function adds constraints to the backend solver.

		@param c: sequence of converted backend objects
		@param s: backend solver object
		'''
		raise NotImplementedError("backend doesn't support solving")

	def check_exprs(self, s, extra_constraints=()):
		'''
		This function does a constraint check.

		@param s: backend solver object
		@param extra_constraints: extra constraints (claripy.E objects) to add
								   to s for this solve
		@returns True or False, depending on satisfiability
		'''
		return self.check(s, extra_constraints=self.convert_list(extra_constraints))

	def check(self, s, extra_constraints=()):
		'''
		This function does a constraint check.

		@param s: backend solver object
		@param extra_constraints: extra constraints (backend objects) to add
								   to s for this solve
		@returns True or False, depending on satisfiability
		'''
		raise NotImplementedError("backend doesn't support solving")

	def results_exprs(self, s, extra_constraints=(), generic_model=None):
		'''
		This function does a constraint check.

		@param s: backend solver object
		@param extra_constraints: extra constraints (claripy.E objects) to add to s for this solve
		@param generic_model: whether or not to create a generic model
		@returns a Result object
		'''
		return self.results(s, extra_constraints=self.convert_list(extra_constraints), generic_model=generic_model)

	def results(self, s, extra_constraints=(), generic_model=None):
		'''
		This function does a constraint check.

		@param s: backend solver object
		@param extra_constraints: extra constraints (backend objects) to add to s for this solve
		@param generic_model: whether or not to create a generic model
		@returns a Result object
		'''
		raise NotImplementedError("backend doesn't support solving")

	def eval_expr(self, s, expr, n, extra_constraints=(), result=None):
		'''
		This function returns up to n possible solutions for expression expr.

		@param s: backend solver object
		@param expr: expression (claripy.E object) to evaluate
		@param n: number of results to return
		@param extra_constraints: extra constraints (claripy.E objects) to add to s for this solve
		@param result: a cached Result from the last constraint solve
		@returns a sequence of up to n results (backend objects)
		'''
		return self.eval(s, self.convert(expr), n, extra_constraints=self.convert_list(extra_constraints), result=result)

	def eval(self, s, expr, n, extra_constraints=(), result=None):
		'''
		This function returns up to n possible solutions for expression expr.

		@param s: backend solver object
		@param expr: expression (backend object) to evaluate
		@param n: number of results to return
		@param extra_constraints: extra constraints (backend objects) to add to s for this solve
		@param result: a cached Result from the last constraint solve
		@returns a sequence of up to n results (backend objects)
		'''
		raise NotImplementedError("backend doesn't support solving")

	def min_expr(self, s, expr, extra_constraints=(), result=None):
		'''
		Return the minimum value of expr.

		@param s: backend solver object
		@param expr: expression (claripy.E object) to evaluate
		@param extra_constraints: extra constraints (claripy.E objects) to add to s for this solve
		@param result: a cached Result from the last constraint solve
		@returns the minimum possible value of expr (backend object)
		'''
		return self.min(s, self.convert(expr), extra_constraints=self.convert_list(extra_constraints), result=result)

	def min(self, s, expr, extra_constraints=(), result=None):
		'''
		Return the minimum value of expr.

		@param s: backend solver object
		@param expr: expression (backend object) to evaluate
		@param extra_constraints: extra constraints (backend objects) to add to s for this solve
		@param result: a cached Result from the last constraint solve
		@returns the minimum possible value of expr (backend object)
		'''
		raise NotImplementedError("backend doesn't support solving")

	def max_expr(self, s, expr, extra_constraints=(), result=None):
		'''
		Return the maximum value of expr.

		@param s: backend solver object
		@param expr: expression (claripy.E object) to evaluate
		@param extra_constraints: extra constraints (claripy.E objects) to add to s for this solve
		@param result: a cached Result from the last constraint solve
		@returns the maximum possible value of expr (backend object)
		'''
		return self.max(s, self.convert(expr), extra_constraints=self.convert_list(extra_constraints), result=result)

	def max(self, s, expr, extra_constraints=(), result=None):
		'''
		Return the maximum value of expr.

		@param s: backend solver object
		@param expr: expression (backend object) to evaluate
		@param extra_constraints: extra constraints (backend objects) to add to s for this solve
		@param result: a cached Result from the last constraint solve
		@returns the maximum possible value of expr (backend object)
		'''
		raise NotImplementedError("backend doesn't support solving")

	def solution_expr(self, s, expr, v, extra_constraints=(), result=None): #pylint:disable=unused-argument
		'''
		Return True if v is a solution of expr with the extra constraints, False otherwise.

		@param s: backend solver object
		@param expr: expression (claripy.E) to evaluate
		@param v: the proposed solution (claripy.E)
		@param extra_constraints: extra constraints (backend objects) to add to s for this solve
		@param result: a cached Result from the last constraint solve
		@returns True if v is a solution of expr, False otherwise
		'''

		return self.check_exprs(s, extra_constraints=(expr==v,) + extra_constraints)

	def solution(self, s, expr, v, extra_constraints=(), result=None): #pylint:disable=unused-argument
		'''
		Return True if v is a solution of expr with the extra constraints, False otherwise.

		@param s: backend solver object
		@param expr: expression (backend object) to evaluate
		@param v: the proposed solution (backend object)
		@param extra_constraints: extra constraints (backend objects) to add to s for this solve
		@param result: a cached Result from the last constraint solve
		@returns True if v is a solution of expr, False otherwise
		'''

		return self.check_exprs(s, extra_constraints=(expr==v,) + extra_constraints)

	def size_expr(self, a, result=None):
		'''
		This should return the size of an expression.

		@param a: the claripy A object
		'''
		return self.size(self.convert(a, result=result))

	def size(self, o, result=None): #pylint:disable=no-self-use,unused-argument
		'''
		This should return the size of an object.

		@param o: the (backend-native) object
		'''
		raise NotImplementedError("backend doesn't support size")

	def name_expr(self, a, result=None):
		'''
		This should return the name of an expression.

		@param a: the claripy A object
		'''
		return self.name(self.convert(a, result=result))

	def name(self, o, result=None): #pylint:disable=no-self-use,unused-argument
		'''
		This should return the name of an object.

		@param o: the (backend-native) object
		'''
		raise NotImplementedError("backend doesn't support name")

	def identical_expr(self, a, b, result=None):
		'''
		This should return whether a is identical to b. Of course, this isn't always
		clear. A True should mean that it is definitely identical. False
		means that, conservitivly, it might not be.

		@param a: a claripy A object
		@param b: a claripy A object
		'''
		return self.identical(self.convert(a, result=result), self.convert(b, result=result))

	def identical(self, a, b, result=None): #pylint:disable=no-self-use,unused-argument
		'''
		This should return whether a is identical to b. Of course, this isn't always
		clear. A True should mean that it is definitely identical. False
		means that, conservitivly, it might not be.

		@param a: the (backend-native) object
		@param b: the (backend-native) object
		'''
		raise NotImplementedError("backend doesn't support name")

class Kinematics_Function:

    def __init__(self):
        pass

    def get_formulas(self):
        return {"1":"V = Vᵢ + at",
                "2":"Δd = (Vᵢ + V)/2 x t",
                "3":"Δd = Vᵢt + ½at²",
                "4":"Δd = Vt - ½at²",
                "5":"V² = Vᵢ² + 2aΔd"}

    def display_formulas(self):
        for val in self.get_formulas():
            print(f"{val}. {self.get_formulas()[val]}")

    def calc_vf_no_d(v_initial,acceleration,time):
        return v_initial + acceleration*time

    def calc_d_no_a(v_initial,v_final,time):
        return (v_initial+v_final)/2 * time

    def calc_d_no_vf(v_initial,acceleration,time):
        return v_initial*time + 0.5((acceleration*time**2))

    def calc_d_no_vi(v_final,acceleration,time):
        return v_final*time - 0.5((acceleration*time**2))

    def calc_vf_no_t(v_initial,acceleration,displacement):
        return (v_initial**2 + 2*acceleration*displacement)**0.5

if __name__ == "__main__":
    obje = Kinematics_Function()
    obje.display_formulas()
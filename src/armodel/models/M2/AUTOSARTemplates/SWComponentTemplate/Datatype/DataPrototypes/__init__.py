"""DataPrototypes module."""
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.application_array_element import (
    ApplicationArrayElement,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.application_record_element import (
    ApplicationRecordElement,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.application_composite_element_data_prototype import (
    ApplicationCompositeElementDataPrototype,
)

__all__ = [
    "ApplicationArrayElement",
    "ApplicationCompositeElementDataPrototype",
    "ApplicationRecordElement",
    "AutosarDataPrototype",
    "DataPrototype",
    "ParameterDataPrototype",
    "VariableDataPrototype",
]

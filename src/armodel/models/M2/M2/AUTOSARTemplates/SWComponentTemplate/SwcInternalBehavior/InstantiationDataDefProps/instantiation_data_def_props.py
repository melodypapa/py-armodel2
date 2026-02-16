"""InstantiationDataDefProps AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_parameter_ref import (
    AutosarParameterRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_variable_ref import (
    AutosarVariableRef,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)


class InstantiationDataDefProps(ARObject):
    """AUTOSAR InstantiationDataDefProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "parameter": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AutosarParameterRef,
        ),  # parameter
        "sw_data_def": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwDataDefProps,
        ),  # swDataDef
        "variable_instance": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AutosarVariableRef,
        ),  # variableInstance
    }

    def __init__(self) -> None:
        """Initialize InstantiationDataDefProps."""
        super().__init__()
        self.parameter: Optional[AutosarParameterRef] = None
        self.sw_data_def: Optional[SwDataDefProps] = None
        self.variable_instance: Optional[AutosarVariableRef] = None


class InstantiationDataDefPropsBuilder:
    """Builder for InstantiationDataDefProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InstantiationDataDefProps = InstantiationDataDefProps()

    def build(self) -> InstantiationDataDefProps:
        """Build and return InstantiationDataDefProps object.

        Returns:
            InstantiationDataDefProps instance
        """
        # TODO: Add validation
        return self._obj

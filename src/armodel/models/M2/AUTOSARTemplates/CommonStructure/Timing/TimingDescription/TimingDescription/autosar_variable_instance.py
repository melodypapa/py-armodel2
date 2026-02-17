"""AutosarVariableInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 85)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class AutosarVariableInstance(Identifiable):
    """AUTOSAR AutosarVariableInstance."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "variable_instance_instance_ref": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DataPrototype,
        ),  # variableInstanceInstanceRef
    }

    def __init__(self) -> None:
        """Initialize AutosarVariableInstance."""
        super().__init__()
        self.variable_instance_instance_ref: Optional[DataPrototype] = None


class AutosarVariableInstanceBuilder:
    """Builder for AutosarVariableInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AutosarVariableInstance = AutosarVariableInstance()

    def build(self) -> AutosarVariableInstance:
        """Build and return AutosarVariableInstance object.

        Returns:
            AutosarVariableInstance instance
        """
        # TODO: Add validation
        return self._obj

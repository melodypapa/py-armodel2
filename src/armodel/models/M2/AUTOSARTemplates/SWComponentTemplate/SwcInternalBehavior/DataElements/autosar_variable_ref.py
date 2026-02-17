"""AutosarVariableRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 307)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 315)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_DataElements.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class AutosarVariableRef(ARObject):
    """AUTOSAR AutosarVariableRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "autosar_variable": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (ArVariableIn),
        ),  # autosarVariable
        "local_variable": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=VariableDataPrototype,
        ),  # localVariable
    }

    def __init__(self) -> None:
        """Initialize AutosarVariableRef."""
        super().__init__()
        self.autosar_variable: Optional[Any] = None
        self.local_variable: Optional[VariableDataPrototype] = None


class AutosarVariableRefBuilder:
    """Builder for AutosarVariableRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AutosarVariableRef = AutosarVariableRef()

    def build(self) -> AutosarVariableRef:
        """Build and return AutosarVariableRef object.

        Returns:
            AutosarVariableRef instance
        """
        # TODO: Add validation
        return self._obj

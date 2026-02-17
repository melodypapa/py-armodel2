"""PerInstanceMemory AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 597)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_PerInstanceMemory.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
    String,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)


class PerInstanceMemory(Identifiable):
    """AUTOSAR PerInstanceMemory."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "init_value": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # initValue
        "sw_data_def": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwDataDefProps,
        ),  # swDataDef
        "type": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # type
        "type_definition": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # typeDefinition
    }

    def __init__(self) -> None:
        """Initialize PerInstanceMemory."""
        super().__init__()
        self.init_value: Optional[String] = None
        self.sw_data_def: Optional[SwDataDefProps] = None
        self.type: Optional[CIdentifier] = None
        self.type_definition: Optional[String] = None


class PerInstanceMemoryBuilder:
    """Builder for PerInstanceMemory."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PerInstanceMemory = PerInstanceMemory()

    def build(self) -> PerInstanceMemory:
        """Build and return PerInstanceMemory object.

        Returns:
            PerInstanceMemory instance
        """
        # TODO: Add validation
        return self._obj

"""TargetIPduRef AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.pdu_mapping_default_value import (
    PduMappingDefaultValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class TargetIPduRef(ARObject):
    """AUTOSAR TargetIPduRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "default_value": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PduMappingDefaultValue,
        ),  # defaultValue
        "target_i_pdu": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PduTriggering,
        ),  # targetIPdu
    }

    def __init__(self) -> None:
        """Initialize TargetIPduRef."""
        super().__init__()
        self.default_value: Optional[PduMappingDefaultValue] = None
        self.target_i_pdu: Optional[PduTriggering] = None


class TargetIPduRefBuilder:
    """Builder for TargetIPduRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TargetIPduRef = TargetIPduRef()

    def build(self) -> TargetIPduRef:
        """Build and return TargetIPduRef object.

        Returns:
            TargetIPduRef instance
        """
        # TODO: Add validation
        return self._obj

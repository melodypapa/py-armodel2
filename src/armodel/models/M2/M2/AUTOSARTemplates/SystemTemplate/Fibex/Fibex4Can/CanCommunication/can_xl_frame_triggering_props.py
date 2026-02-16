"""CanXlFrameTriggeringProps AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CanXlFrameTriggeringProps(ARObject):
    """AUTOSAR CanXlFrameTriggeringProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "acceptance_field": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # acceptanceField
        "priority_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # priorityId
        "sdu_type": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # sduType
        "vcid": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # vcid
    }

    def __init__(self) -> None:
        """Initialize CanXlFrameTriggeringProps."""
        super().__init__()
        self.acceptance_field: Optional[PositiveInteger] = None
        self.priority_id: Optional[PositiveInteger] = None
        self.sdu_type: Optional[PositiveInteger] = None
        self.vcid: Optional[PositiveInteger] = None


class CanXlFrameTriggeringPropsBuilder:
    """Builder for CanXlFrameTriggeringProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanXlFrameTriggeringProps = CanXlFrameTriggeringProps()

    def build(self) -> CanXlFrameTriggeringProps:
        """Build and return CanXlFrameTriggeringProps object.

        Returns:
            CanXlFrameTriggeringProps instance
        """
        # TODO: Add validation
        return self._obj

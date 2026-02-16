"""TagWithOptionalValue AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    String,
)


class TagWithOptionalValue(ARObject):
    """AUTOSAR TagWithOptionalValue."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "key": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # key
        "sequence_offset": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # sequenceOffset
        "value": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # value
    }

    def __init__(self) -> None:
        """Initialize TagWithOptionalValue."""
        super().__init__()
        self.key: Optional[String] = None
        self.sequence_offset: Optional[Integer] = None
        self.value: Optional[String] = None


class TagWithOptionalValueBuilder:
    """Builder for TagWithOptionalValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TagWithOptionalValue = TagWithOptionalValue()

    def build(self) -> TagWithOptionalValue:
        """Build and return TagWithOptionalValue object.

        Returns:
            TagWithOptionalValue instance
        """
        # TODO: Add validation
        return self._obj

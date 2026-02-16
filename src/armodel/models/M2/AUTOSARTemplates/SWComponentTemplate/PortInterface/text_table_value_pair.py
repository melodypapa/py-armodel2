"""TextTableValuePair AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)


class TextTableValuePair(ARObject):
    """AUTOSAR TextTableValuePair."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "first_value": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # firstValue
        "second_value": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # secondValue
    }

    def __init__(self) -> None:
        """Initialize TextTableValuePair."""
        super().__init__()
        self.first_value: Optional[Numerical] = None
        self.second_value: Optional[Numerical] = None


class TextTableValuePairBuilder:
    """Builder for TextTableValuePair."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TextTableValuePair = TextTableValuePair()

    def build(self) -> TextTableValuePair:
        """Build and return TextTableValuePair object.

        Returns:
            TextTableValuePair instance
        """
        # TODO: Add validation
        return self._obj

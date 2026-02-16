"""TextValueSpecification AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    VerbatimString,
)


class TextValueSpecification(ValueSpecification):
    """AUTOSAR TextValueSpecification."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "value": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # value
    }

    def __init__(self) -> None:
        """Initialize TextValueSpecification."""
        super().__init__()
        self.value: Optional[VerbatimString] = None


class TextValueSpecificationBuilder:
    """Builder for TextValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TextValueSpecification = TextValueSpecification()

    def build(self) -> TextValueSpecification:
        """Build and return TextValueSpecification object.

        Returns:
            TextValueSpecification instance
        """
        # TODO: Add validation
        return self._obj

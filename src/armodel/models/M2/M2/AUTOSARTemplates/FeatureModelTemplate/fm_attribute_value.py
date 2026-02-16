"""FMAttributeValue AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_attribute_def import (
    FMAttributeDef,
)


class FMAttributeValue(ARObject):
    """AUTOSAR FMAttributeValue."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "definition": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=FMAttributeDef,
        ),  # definition
        "value": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # value
    }

    def __init__(self) -> None:
        """Initialize FMAttributeValue."""
        super().__init__()
        self.definition: Optional[FMAttributeDef] = None
        self.value: Optional[Numerical] = None


class FMAttributeValueBuilder:
    """Builder for FMAttributeValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMAttributeValue = FMAttributeValue()

    def build(self) -> FMAttributeValue:
        """Build and return FMAttributeValue object.

        Returns:
            FMAttributeValue instance
        """
        # TODO: Add validation
        return self._obj

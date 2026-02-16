"""AttributeValueVariationPoint AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PrimitiveIdentifier,
    String,
)


class AttributeValueVariationPoint(ARObject):
    """AUTOSAR AttributeValueVariationPoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "binding_time_enum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=BindingTimeEnum,
        ),  # bindingTimeEnum
        "blueprint_value": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # blueprintValue
        "sd": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # sd
        "short_label": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # shortLabel
    }

    def __init__(self) -> None:
        """Initialize AttributeValueVariationPoint."""
        super().__init__()
        self.binding_time_enum: Optional[BindingTimeEnum] = None
        self.blueprint_value: Optional[String] = None
        self.sd: Optional[String] = None
        self.short_label: Optional[PrimitiveIdentifier] = None


class AttributeValueVariationPointBuilder:
    """Builder for AttributeValueVariationPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AttributeValueVariationPoint = AttributeValueVariationPoint()

    def build(self) -> AttributeValueVariationPoint:
        """Build and return AttributeValueVariationPoint object.

        Returns:
            AttributeValueVariationPoint instance
        """
        # TODO: Add validation
        return self._obj

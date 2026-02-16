"""ParameterPortAnnotation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)


class ParameterPortAnnotation(GeneralAnnotation):
    """AUTOSAR ParameterPortAnnotation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("parameter", None, False, False, ParameterDataPrototype),  # parameter
    ]

    def __init__(self) -> None:
        """Initialize ParameterPortAnnotation."""
        super().__init__()
        self.parameter: Optional[ParameterDataPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ParameterPortAnnotation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ParameterPortAnnotation":
        """Create ParameterPortAnnotation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ParameterPortAnnotation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ParameterPortAnnotation since parent returns ARObject
        return cast("ParameterPortAnnotation", obj)


class ParameterPortAnnotationBuilder:
    """Builder for ParameterPortAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ParameterPortAnnotation = ParameterPortAnnotation()

    def build(self) -> ParameterPortAnnotation:
        """Build and return ParameterPortAnnotation object.

        Returns:
            ParameterPortAnnotation instance
        """
        # TODO: Add validation
        return self._obj

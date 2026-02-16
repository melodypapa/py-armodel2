"""SenderReceiverAnnotation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class SenderReceiverAnnotation(GeneralAnnotation):
    """AUTOSAR SenderReceiverAnnotation."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("computed", None, True, False, None),  # computed
        ("data_element", None, False, False, VariableDataPrototype),  # dataElement
        ("limit_kind", None, False, False, DataLimitKindEnum),  # limitKind
        ("processing_kind_enum", None, False, False, ProcessingKindEnum),  # processingKindEnum
    ]

    def __init__(self) -> None:
        """Initialize SenderReceiverAnnotation."""
        super().__init__()
        self.computed: Optional[Boolean] = None
        self.data_element: Optional[VariableDataPrototype] = None
        self.limit_kind: Optional[DataLimitKindEnum] = None
        self.processing_kind_enum: Optional[ProcessingKindEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SenderReceiverAnnotation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderReceiverAnnotation":
        """Create SenderReceiverAnnotation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SenderReceiverAnnotation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SenderReceiverAnnotation since parent returns ARObject
        return cast("SenderReceiverAnnotation", obj)


class SenderReceiverAnnotationBuilder:
    """Builder for SenderReceiverAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderReceiverAnnotation = SenderReceiverAnnotation()

    def build(self) -> SenderReceiverAnnotation:
        """Build and return SenderReceiverAnnotation object.

        Returns:
            SenderReceiverAnnotation instance
        """
        # TODO: Add validation
        return self._obj

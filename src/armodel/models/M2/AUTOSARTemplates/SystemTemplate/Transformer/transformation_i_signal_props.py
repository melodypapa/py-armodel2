"""TransformationISignalProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class TransformationISignalProps(ARObject):
    """AUTOSAR TransformationISignalProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("cs_error_reaction", None, False, False, CSTransformerErrorReactionEnum),  # csErrorReaction
        ("data_prototypes", None, False, True, DataPrototype),  # dataPrototypes
        ("transformer", None, False, False, any (Transformation)),  # transformer
    ]

    def __init__(self) -> None:
        """Initialize TransformationISignalProps."""
        super().__init__()
        self.cs_error_reaction: Optional[CSTransformerErrorReactionEnum] = None
        self.data_prototypes: list[DataPrototype] = []
        self.transformer: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TransformationISignalProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransformationISignalProps":
        """Create TransformationISignalProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TransformationISignalProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TransformationISignalProps since parent returns ARObject
        return cast("TransformationISignalProps", obj)


class TransformationISignalPropsBuilder:
    """Builder for TransformationISignalProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransformationISignalProps = TransformationISignalProps()

    def build(self) -> TransformationISignalProps:
        """Build and return TransformationISignalProps object.

        Returns:
            TransformationISignalProps instance
        """
        # TODO: Add validation
        return self._obj

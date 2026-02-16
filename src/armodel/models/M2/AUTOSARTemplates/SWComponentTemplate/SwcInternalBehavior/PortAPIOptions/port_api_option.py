"""PortAPIOption AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_transformation import (
    DataTransformation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.port_defined_argument_value import (
    PortDefinedArgumentValue,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.swc_supported_feature import (
    SwcSupportedFeature,
)


class PortAPIOption(ARObject):
    """AUTOSAR PortAPIOption."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("enable_take", None, True, False, None),  # enableTake
        ("error_handling", None, False, False, DataTransformation),  # errorHandling
        ("indirect_api", None, True, False, None),  # indirectAPI
        ("port", None, False, False, PortPrototype),  # port
        ("port_arg_values", None, False, True, PortDefinedArgumentValue),  # portArgValues
        ("supporteds", None, False, True, SwcSupportedFeature),  # supporteds
        ("transformer", None, False, False, DataTransformation),  # transformer
    ]

    def __init__(self) -> None:
        """Initialize PortAPIOption."""
        super().__init__()
        self.enable_take: Optional[Boolean] = None
        self.error_handling: Optional[DataTransformation] = None
        self.indirect_api: Optional[Boolean] = None
        self.port: Optional[PortPrototype] = None
        self.port_arg_values: list[PortDefinedArgumentValue] = []
        self.supporteds: list[SwcSupportedFeature] = []
        self.transformer: Optional[DataTransformation] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PortAPIOption to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PortAPIOption":
        """Create PortAPIOption from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PortAPIOption instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PortAPIOption since parent returns ARObject
        return cast("PortAPIOption", obj)


class PortAPIOptionBuilder:
    """Builder for PortAPIOption."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortAPIOption = PortAPIOption()

    def build(self) -> PortAPIOption:
        """Build and return PortAPIOption object.

        Returns:
            PortAPIOption instance
        """
        # TODO: Add validation
        return self._obj

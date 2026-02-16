"""LinSlaveConfig AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_configurable_frame import (
    LinConfigurableFrame,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_error_response import (
    LinErrorResponse,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_ordered_configurable_frame import (
    LinOrderedConfigurableFrame,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_slave_config_ident import (
    LinSlaveConfigIdent,
)


class LinSlaveConfig(ARObject):
    """AUTOSAR LinSlaveConfig."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("configured_nad", None, True, False, None),  # configuredNad
        ("function_id", None, True, False, None),  # functionId
        ("ident", None, False, False, LinSlaveConfigIdent),  # ident
        ("initial_nad", None, True, False, None),  # initialNad
        ("lin_configurable_frames", None, False, True, LinConfigurableFrame),  # linConfigurableFrames
        ("lin_error_response", None, False, False, LinErrorResponse),  # linErrorResponse
        ("lin_ordereds", None, False, True, LinOrderedConfigurableFrame),  # linOrdereds
        ("protocol_version", None, True, False, None),  # protocolVersion
        ("supplier_id", None, True, False, None),  # supplierId
        ("variant_id", None, True, False, None),  # variantId
    ]

    def __init__(self) -> None:
        """Initialize LinSlaveConfig."""
        super().__init__()
        self.configured_nad: Optional[Integer] = None
        self.function_id: Optional[PositiveInteger] = None
        self.ident: Optional[LinSlaveConfigIdent] = None
        self.initial_nad: Optional[Integer] = None
        self.lin_configurable_frames: list[LinConfigurableFrame] = []
        self.lin_error_response: Optional[LinErrorResponse] = None
        self.lin_ordereds: list[LinOrderedConfigurableFrame] = []
        self.protocol_version: Optional[String] = None
        self.supplier_id: Optional[PositiveInteger] = None
        self.variant_id: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert LinSlaveConfig to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinSlaveConfig":
        """Create LinSlaveConfig from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            LinSlaveConfig instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to LinSlaveConfig since parent returns ARObject
        return cast("LinSlaveConfig", obj)


class LinSlaveConfigBuilder:
    """Builder for LinSlaveConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinSlaveConfig = LinSlaveConfig()

    def build(self) -> LinSlaveConfig:
        """Build and return LinSlaveConfig object.

        Returns:
            LinSlaveConfig instance
        """
        # TODO: Add validation
        return self._obj

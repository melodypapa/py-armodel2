"""GlobalTimeMaster AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)


class GlobalTimeMaster(Identifiable):
    """AUTOSAR GlobalTimeMaster."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("communication_connector", None, False, False, CommunicationConnector),  # communicationConnector
        ("icv_secured", None, False, False, GlobalTimeIcvSupportEnum),  # icvSecured
        ("immediate", None, True, False, None),  # immediate
        ("is_system_wide", None, True, False, None),  # isSystemWide
        ("sync_period", None, True, False, None),  # syncPeriod
    ]

    def __init__(self) -> None:
        """Initialize GlobalTimeMaster."""
        super().__init__()
        self.communication_connector: Optional[CommunicationConnector] = None
        self.icv_secured: Optional[GlobalTimeIcvSupportEnum] = None
        self.immediate: Optional[TimeValue] = None
        self.is_system_wide: Optional[Boolean] = None
        self.sync_period: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert GlobalTimeMaster to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeMaster":
        """Create GlobalTimeMaster from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            GlobalTimeMaster instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to GlobalTimeMaster since parent returns ARObject
        return cast("GlobalTimeMaster", obj)


class GlobalTimeMasterBuilder:
    """Builder for GlobalTimeMaster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeMaster = GlobalTimeMaster()

    def build(self) -> GlobalTimeMaster:
        """Build and return GlobalTimeMaster object.

        Returns:
            GlobalTimeMaster instance
        """
        # TODO: Add validation
        return self._obj

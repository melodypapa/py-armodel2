"""GlobalTimeMaster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 860)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime import (
    GlobalTimeIcvSupportEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)
from abc import ABC, abstractmethod


class GlobalTimeMaster(Identifiable, ABC):
    """AUTOSAR GlobalTimeMaster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    communication_connector: Optional[CommunicationConnector]
    icv_secured: Optional[GlobalTimeIcvSupportEnum]
    immediate: Optional[TimeValue]
    is_system_wide: Optional[Boolean]
    sync_period: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize GlobalTimeMaster."""
        super().__init__()
        self.communication_connector: Optional[CommunicationConnector] = None
        self.icv_secured: Optional[GlobalTimeIcvSupportEnum] = None
        self.immediate: Optional[TimeValue] = None
        self.is_system_wide: Optional[Boolean] = None
        self.sync_period: Optional[TimeValue] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeMaster":
        """Deserialize XML element to GlobalTimeMaster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GlobalTimeMaster object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse communication_connector
        child = ARObject._find_child_element(element, "COMMUNICATION-CONNECTOR")
        if child is not None:
            communication_connector_value = ARObject._deserialize_by_tag(child, "CommunicationConnector")
            obj.communication_connector = communication_connector_value

        # Parse icv_secured
        child = ARObject._find_child_element(element, "ICV-SECURED")
        if child is not None:
            icv_secured_value = child.text
            obj.icv_secured = icv_secured_value

        # Parse immediate
        child = ARObject._find_child_element(element, "IMMEDIATE")
        if child is not None:
            immediate_value = child.text
            obj.immediate = immediate_value

        # Parse is_system_wide
        child = ARObject._find_child_element(element, "IS-SYSTEM-WIDE")
        if child is not None:
            is_system_wide_value = child.text
            obj.is_system_wide = is_system_wide_value

        # Parse sync_period
        child = ARObject._find_child_element(element, "SYNC-PERIOD")
        if child is not None:
            sync_period_value = child.text
            obj.sync_period = sync_period_value

        return obj



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

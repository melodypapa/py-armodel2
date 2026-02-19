"""RtePluginProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 971)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_FlatMap.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_container_value import (
    EcucContainerValue,
)


class RtePluginProps(ARObject):
    """AUTOSAR RtePluginProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    associated: Optional[EcucContainerValue]
    associated_rte: Optional[EcucContainerValue]
    def __init__(self) -> None:
        """Initialize RtePluginProps."""
        super().__init__()
        self.associated: Optional[EcucContainerValue] = None
        self.associated_rte: Optional[EcucContainerValue] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RtePluginProps":
        """Deserialize XML element to RtePluginProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RtePluginProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse associated
        child = ARObject._find_child_element(element, "ASSOCIATED")
        if child is not None:
            associated_value = ARObject._deserialize_by_tag(child, "EcucContainerValue")
            obj.associated = associated_value

        # Parse associated_rte
        child = ARObject._find_child_element(element, "ASSOCIATED-RTE")
        if child is not None:
            associated_rte_value = ARObject._deserialize_by_tag(child, "EcucContainerValue")
            obj.associated_rte = associated_rte_value

        return obj



class RtePluginPropsBuilder:
    """Builder for RtePluginProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RtePluginProps = RtePluginProps()

    def build(self) -> RtePluginProps:
        """Build and return RtePluginProps object.

        Returns:
            RtePluginProps instance
        """
        # TODO: Add validation
        return self._obj

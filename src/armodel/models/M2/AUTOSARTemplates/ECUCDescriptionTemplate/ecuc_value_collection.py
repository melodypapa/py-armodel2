"""EcucValueCollection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 108)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2022)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 222)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)


class EcucValueCollection(ARElement):
    """AUTOSAR EcucValueCollection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ecuc_values: list[Any]
    ecu_extract: Optional[System]
    def __init__(self) -> None:
        """Initialize EcucValueCollection."""
        super().__init__()
        self.ecuc_values: list[Any] = []
        self.ecu_extract: Optional[System] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucValueCollection":
        """Deserialize XML element to EcucValueCollection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucValueCollection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucValueCollection, cls).deserialize(element)

        # Parse ecuc_values (list from container "ECUC-VALUES")
        obj.ecuc_values = []
        container = ARObject._find_child_element(element, "ECUC-VALUES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ecuc_values.append(child_value)

        # Parse ecu_extract
        child = ARObject._find_child_element(element, "ECU-EXTRACT")
        if child is not None:
            ecu_extract_value = ARObject._deserialize_by_tag(child, "System")
            obj.ecu_extract = ecu_extract_value

        return obj



class EcucValueCollectionBuilder:
    """Builder for EcucValueCollection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucValueCollection = EcucValueCollection()

    def build(self) -> EcucValueCollection:
        """Build and return EcucValueCollection object.

        Returns:
            EcucValueCollection instance
        """
        # TODO: Add validation
        return self._obj

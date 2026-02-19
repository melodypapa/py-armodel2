"""SecureCommunicationFreshnessProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 370)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class SecureCommunicationFreshnessProps(Identifiable):
    """AUTOSAR SecureCommunicationFreshnessProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    freshness: Optional[PositiveInteger]
    freshness_value: Optional[PositiveInteger]
    use_freshness: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize SecureCommunicationFreshnessProps."""
        super().__init__()
        self.freshness: Optional[PositiveInteger] = None
        self.freshness_value: Optional[PositiveInteger] = None
        self.use_freshness: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecureCommunicationFreshnessProps":
        """Deserialize XML element to SecureCommunicationFreshnessProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecureCommunicationFreshnessProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse freshness
        child = ARObject._find_child_element(element, "FRESHNESS")
        if child is not None:
            freshness_value = child.text
            obj.freshness = freshness_value

        # Parse freshness_value
        child = ARObject._find_child_element(element, "FRESHNESS-VALUE")
        if child is not None:
            freshness_value_value = child.text
            obj.freshness_value = freshness_value_value

        # Parse use_freshness
        child = ARObject._find_child_element(element, "USE-FRESHNESS")
        if child is not None:
            use_freshness_value = child.text
            obj.use_freshness = use_freshness_value

        return obj



class SecureCommunicationFreshnessPropsBuilder:
    """Builder for SecureCommunicationFreshnessProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecureCommunicationFreshnessProps = SecureCommunicationFreshnessProps()

    def build(self) -> SecureCommunicationFreshnessProps:
        """Build and return SecureCommunicationFreshnessProps object.

        Returns:
            SecureCommunicationFreshnessProps instance
        """
        # TODO: Add validation
        return self._obj

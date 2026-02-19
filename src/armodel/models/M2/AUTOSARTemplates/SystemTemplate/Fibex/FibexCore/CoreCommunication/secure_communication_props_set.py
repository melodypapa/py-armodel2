"""SecureCommunicationPropsSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 370)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class SecureCommunicationPropsSet(FibexElement):
    """AUTOSAR SecureCommunicationPropsSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    authentications: list[Any]
    freshness_propses: list[Any]
    def __init__(self) -> None:
        """Initialize SecureCommunicationPropsSet."""
        super().__init__()
        self.authentications: list[Any] = []
        self.freshness_propses: list[Any] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecureCommunicationPropsSet":
        """Deserialize XML element to SecureCommunicationPropsSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecureCommunicationPropsSet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse authentications (list)
        obj.authentications = []
        for child in ARObject._find_all_child_elements(element, "AUTHENTICATIONS"):
            authentications_value = child.text
            obj.authentications.append(authentications_value)

        # Parse freshness_propses (list)
        obj.freshness_propses = []
        for child in ARObject._find_all_child_elements(element, "FRESHNESS-PROPSES"):
            freshness_propses_value = child.text
            obj.freshness_propses.append(freshness_propses_value)

        return obj



class SecureCommunicationPropsSetBuilder:
    """Builder for SecureCommunicationPropsSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecureCommunicationPropsSet = SecureCommunicationPropsSet()

    def build(self) -> SecureCommunicationPropsSet:
        """Build and return SecureCommunicationPropsSet object.

        Returns:
            SecureCommunicationPropsSet instance
        """
        # TODO: Add validation
        return self._obj

"""SignalServiceTranslationPropsSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 730)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_SignalServiceTranslation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class SignalServiceTranslationPropsSet(ARElement):
    """AUTOSAR SignalServiceTranslationPropsSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    signal_service_propses: list[Any]
    def __init__(self) -> None:
        """Initialize SignalServiceTranslationPropsSet."""
        super().__init__()
        self.signal_service_propses: list[Any] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SignalServiceTranslationPropsSet":
        """Deserialize XML element to SignalServiceTranslationPropsSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SignalServiceTranslationPropsSet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse signal_service_propses (list)
        obj.signal_service_propses = []
        for child in ARObject._find_all_child_elements(element, "SIGNAL-SERVICE-PROPSES"):
            signal_service_propses_value = child.text
            obj.signal_service_propses.append(signal_service_propses_value)

        return obj



class SignalServiceTranslationPropsSetBuilder:
    """Builder for SignalServiceTranslationPropsSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SignalServiceTranslationPropsSet = SignalServiceTranslationPropsSet()

    def build(self) -> SignalServiceTranslationPropsSet:
        """Build and return SignalServiceTranslationPropsSet object.

        Returns:
            SignalServiceTranslationPropsSet instance
        """
        # TODO: Add validation
        return self._obj

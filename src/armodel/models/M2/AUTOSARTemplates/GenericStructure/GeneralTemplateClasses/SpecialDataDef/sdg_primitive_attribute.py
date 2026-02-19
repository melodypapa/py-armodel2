"""SdgPrimitiveAttribute AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 100)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_SpecialDataDef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_abstract_primitive_attribute import (
    SdgAbstractPrimitiveAttribute,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class SdgPrimitiveAttribute(SdgAbstractPrimitiveAttribute):
    """AUTOSAR SdgPrimitiveAttribute."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize SdgPrimitiveAttribute."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgPrimitiveAttribute":
        """Deserialize XML element to SdgPrimitiveAttribute object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SdgPrimitiveAttribute object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        return obj



class SdgPrimitiveAttributeBuilder:
    """Builder for SdgPrimitiveAttribute."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgPrimitiveAttribute = SdgPrimitiveAttribute()

    def build(self) -> SdgPrimitiveAttribute:
        """Build and return SdgPrimitiveAttribute object.

        Returns:
            SdgPrimitiveAttribute instance
        """
        # TODO: Add validation
        return self._obj

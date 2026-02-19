"""DataPrototypeReference AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 787)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from abc import ABC, abstractmethod


class DataPrototypeReference(ARObject, ABC):
    """AUTOSAR DataPrototypeReference."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    tag_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DataPrototypeReference."""
        super().__init__()
        self.tag_id: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataPrototypeReference":
        """Deserialize XML element to DataPrototypeReference object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataPrototypeReference object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse tag_id
        child = ARObject._find_child_element(element, "TAG-ID")
        if child is not None:
            tag_id_value = child.text
            obj.tag_id = tag_id_value

        return obj



class DataPrototypeReferenceBuilder:
    """Builder for DataPrototypeReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeReference = DataPrototypeReference()

    def build(self) -> DataPrototypeReference:
        """Build and return DataPrototypeReference object.

        Returns:
            DataPrototypeReference instance
        """
        # TODO: Add validation
        return self._obj

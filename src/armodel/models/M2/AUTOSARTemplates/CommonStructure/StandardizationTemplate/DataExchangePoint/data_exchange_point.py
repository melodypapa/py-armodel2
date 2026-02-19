"""DataExchangePoint AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 78)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.baseline import (
    Baseline,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.data_format_tailoring import (
    DataFormatTailoring,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchange.specification_scope import (
    SpecificationScope,
)


class DataExchangePoint(ARElement):
    """AUTOSAR DataExchangePoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_format: Optional[DataFormatTailoring]
    kind: DataExchangePoint
    referenced: Baseline
    specification_scope: Optional[SpecificationScope]
    def __init__(self) -> None:
        """Initialize DataExchangePoint."""
        super().__init__()
        self.data_format: Optional[DataFormatTailoring] = None
        self.kind: DataExchangePoint = None
        self.referenced: Baseline = None
        self.specification_scope: Optional[SpecificationScope] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataExchangePoint":
        """Deserialize XML element to DataExchangePoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataExchangePoint object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_format
        child = ARObject._find_child_element(element, "DATA-FORMAT")
        if child is not None:
            data_format_value = ARObject._deserialize_by_tag(child, "DataFormatTailoring")
            obj.data_format = data_format_value

        # Parse kind
        child = ARObject._find_child_element(element, "KIND")
        if child is not None:
            kind_value = ARObject._deserialize_by_tag(child, "DataExchangePoint")
            obj.kind = kind_value

        # Parse referenced
        child = ARObject._find_child_element(element, "REFERENCED")
        if child is not None:
            referenced_value = ARObject._deserialize_by_tag(child, "Baseline")
            obj.referenced = referenced_value

        # Parse specification_scope
        child = ARObject._find_child_element(element, "SPECIFICATION-SCOPE")
        if child is not None:
            specification_scope_value = ARObject._deserialize_by_tag(child, "SpecificationScope")
            obj.specification_scope = specification_scope_value

        return obj



class DataExchangePointBuilder:
    """Builder for DataExchangePoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataExchangePoint = DataExchangePoint()

    def build(self) -> DataExchangePoint:
        """Build and return DataExchangePoint object.

        Returns:
            DataExchangePoint instance
        """
        # TODO: Add validation
        return self._obj

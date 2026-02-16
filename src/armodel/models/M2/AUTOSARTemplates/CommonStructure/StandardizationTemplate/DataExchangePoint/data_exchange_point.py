"""DataExchangePoint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.baseline import (
    Baseline,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.data_exchange_point import (
    DataExchangePoint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.data_format_tailoring import (
    DataFormatTailoring,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchange.specification_scope import (
    SpecificationScope,
)


class DataExchangePoint(ARElement):
    """AUTOSAR DataExchangePoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_format", None, False, False, DataFormatTailoring),  # dataFormat
        ("kind", None, False, False, DataExchangePoint),  # kind
        ("referenced", None, False, False, Baseline),  # referenced
        ("specification_scope", None, False, False, SpecificationScope),  # specificationScope
    ]

    def __init__(self) -> None:
        """Initialize DataExchangePoint."""
        super().__init__()
        self.data_format: Optional[DataFormatTailoring] = None
        self.kind: DataExchangePoint = None
        self.referenced: Baseline = None
        self.specification_scope: Optional[SpecificationScope] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DataExchangePoint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataExchangePoint":
        """Create DataExchangePoint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DataExchangePoint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DataExchangePoint since parent returns ARObject
        return cast("DataExchangePoint", obj)


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

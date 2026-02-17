"""DataExchangePoint AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "data_format": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DataFormatTailoring,
        ),  # dataFormat
        "kind": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=DataExchangePoint,
        ),  # kind
        "referenced": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=Baseline,
        ),  # referenced
        "specification_scope": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SpecificationScope,
        ),  # specificationScope
    }

    def __init__(self) -> None:
        """Initialize DataExchangePoint."""
        super().__init__()
        self.data_format: Optional[DataFormatTailoring] = None
        self.kind: DataExchangePoint = None
        self.referenced: Baseline = None
        self.specification_scope: Optional[SpecificationScope] = None


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

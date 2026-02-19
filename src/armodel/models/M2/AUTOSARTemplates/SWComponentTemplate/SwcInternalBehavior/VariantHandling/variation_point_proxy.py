"""VariationPointProxy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 613)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 479)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.condition_by_formula import (
    ConditionByFormula,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type import (
        AbstractImplementationDataType,
    )



class VariationPointProxy(Identifiable):
    """AUTOSAR VariationPointProxy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    condition_access: Optional[ConditionByFormula]
    implementation: Optional[AbstractImplementationDataType]
    post_build_value: Optional[Any]
    def __init__(self) -> None:
        """Initialize VariationPointProxy."""
        super().__init__()
        self.condition_access: Optional[ConditionByFormula] = None
        self.implementation: Optional[AbstractImplementationDataType] = None
        self.post_build_value: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "VariationPointProxy":
        """Deserialize XML element to VariationPointProxy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized VariationPointProxy object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(VariationPointProxy, cls).deserialize(element)

        # Parse condition_access
        child = ARObject._find_child_element(element, "CONDITION-ACCESS")
        if child is not None:
            condition_access_value = ARObject._deserialize_by_tag(child, "ConditionByFormula")
            obj.condition_access = condition_access_value

        # Parse implementation
        child = ARObject._find_child_element(element, "IMPLEMENTATION")
        if child is not None:
            implementation_value = ARObject._deserialize_by_tag(child, "AbstractImplementationDataType")
            obj.implementation = implementation_value

        # Parse post_build_value
        child = ARObject._find_child_element(element, "POST-BUILD-VALUE")
        if child is not None:
            post_build_value_value = child.text
            obj.post_build_value = post_build_value_value

        return obj



class VariationPointProxyBuilder:
    """Builder for VariationPointProxy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VariationPointProxy = VariationPointProxy()

    def build(self) -> VariationPointProxy:
        """Build and return VariationPointProxy object.

        Returns:
            VariationPointProxy instance
        """
        # TODO: Add validation
        return self._obj

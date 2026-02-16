"""VariationPointProxy AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type import (
    AbstractImplementationDataType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.condition_by_formula import (
    ConditionByFormula,
)


class VariationPointProxy(Identifiable):
    """AUTOSAR VariationPointProxy."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("condition_access", None, False, False, ConditionByFormula),  # conditionAccess
        ("implementation", None, False, False, AbstractImplementationDataType),  # implementation
        ("post_build_value", None, False, False, any (PostBuildVariant)),  # postBuildValue
    ]

    def __init__(self) -> None:
        """Initialize VariationPointProxy."""
        super().__init__()
        self.condition_access: Optional[ConditionByFormula] = None
        self.implementation: Optional[AbstractImplementationDataType] = None
        self.post_build_value: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert VariationPointProxy to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "VariationPointProxy":
        """Create VariationPointProxy from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            VariationPointProxy instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to VariationPointProxy since parent returns ARObject
        return cast("VariationPointProxy", obj)


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
